

///////////////////API CALL///////////////////////

class APICALL {
    constructor (params, endpoint, callback){
        this.payload = params
        this.build(endpoint)
        this.send(params, '/API/RESTful/', callback)
    }

    build (endpoint) {
        this.payload.API = endpoint
    }

    send (params, endpointURL, callback) {
        const request = new XMLHttpRequest();
        const queryString = new URLSearchParams(params).toString();
        const url = `${endpointURL}?${queryString}`;
        request.open("GET", url);

        const csrftoken = getCookie('csrftoken');

        request.setRequestHeader('X-CSRFToken', csrftoken);
    
        request.onreadystatechange = function () {
            if (request.readyState === XMLHttpRequest.DONE) {
                if (request.status === 200) {
                    console.log('Data requested successfully');
                    const response = JSON.parse(request.responseText);
                    callback(response.response);
                } else {
                    console.error('Error requesting data:', request.status);
                }
            }
        };
    
        request.send();

    }



}





const conferenceSelector = document.getElementById('conferenceSelector');

function fetchConferences(conferences) {
    conferences.forEach(item => {
        console.log(item)
        console.log(item.Conference)
        const newOption = document.createElement('option');
        newOption.value = item.Conference
        newOption.textContent = item.Conference;
        conferenceSelector.appendChild(newOption);
    });
}


let params = {conference: "conferences"}

let confs = new APICALL(params, "pwr_5_teams", fetchConferences)




function handleResponse(data) {
    const resultContainer = document.getElementById('resultContainer');
    resultContainer.innerHTML = ''; 

    data.forEach(item => {
        const newItemElement = document.createElement('div');
        newItemElement.textContent = item.Team;
        resultContainer.appendChild(newItemElement);
    });
}

function fetchData() {
    const selectedConference = conferenceSelector.value;

    // Make a new APICALL based on the selected conference
    let params = { conference: selectedConference };
    let pwr5teams = new APICALL(params, "pwr_5_teams", handleResponse);
}



document.getElementById('fetchDataBtn').addEventListener('click', fetchData);




