import os
import time
from datetime import datetime
import json
from google.cloud import storage
from google.auth.exceptions import RefreshError


class Webhook():
    def __init__(self, get_response):
        self.get_response = get_response
        self.templates = [

        ]# Filter request ingestion to only include these templates

    def __call__(self, request):
        _t = time.time() 
        response = self.get_response(request)
        _t = int((time.time() - _t)*1000)# Calculated execution time.

        #Filter
        if self.templates and not list(filter(request.get_full_path().startswith, self.templates)): 
            return response 

        # generate payload
        payload = {
            "endpoint": request.get_full_path(),
            "response_code": response.status_code,
            "method": request.method,
            "remote_address": self.get_client_ip(request),
            "exececution_time": _t
        }

        self.ingest(payload)

        return response

    # get clients ip address
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            _ip = x_forwarded_for.split(',')[0]
        else:
            _ip = request.META.get('REMOTE_ADDR')
        return _ip

    def ingest(self, payload):
        pass#push payload to specified endpoint(s)

    

class GCS(Webhook):
    def __init__(self, get_response) -> None:
        super().__init__(get_response)

    def ingest(self, payload):
        client = storage.Client('portfolio-project-353016')

        attempt = 0
        while True:
            attempt += 1
            try:
                bucket = client.get_bucket('osteensco_portfolio_site_bucket')
                break
            except RefreshError:
                os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = json.loads(os.environ.get('GCBucketServiceKey'))
                if attempt > 1: 
                    return None
        
        blob = bucket.blob(f'''traffic/{datetime.now()})''')
        blob.upload_from_string(
            data=json.dumps(payload),
            content_type='application/json'
        )
        

