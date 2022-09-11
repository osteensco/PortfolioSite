
/////////////////cookies///////////////////
let types = [
    ['id', 3650],
    ['sessionID', 0],

]

function setExpiration(type) {
    for (i = 0; i < types.length; i++) {
        if (types[i][0] == type) {
            return types[i][1]
        }
    }

}

class Cookie {
    constructor (type) {
        this.type = type
        this.datetime = new Date()
        this.expires = this.expiration(type)
        this.value = this.read(type)

    }

    generateID() {
        let elem = [
            this.datetime.getUTCDate(),
            this.datetime.getUTCMonth(),
            this.datetime.getUTCFullYear(),
            this.datetime.getTime(),
            `${Math.random()*100 + Math.random()*100 }`,
        ]
        return `${this.type}${elem[0]}${elem[1]}${elem[2]}${elem[3]}${elem[4]}`
    }

    expiration(type) {
        let days = setExpiration(type)
        if (days > 0) {
            const d = new Date()
            d.setTime(d.getTime() + (days*24*60*60*1000))
            return d.toUTCString()
        } else {
            return false
        }
        
    }

    set(field,value,exdays) {
        if (exdays != 0) {
            let exp = "expires=" + exdays
            document.cookie = field + "=" + value + ";" + exp
        } else {//cookie should expire on browser close if not listed
            document.cookie = field + "=" + value 
        }

    }
  
    get(field) {
        let name = field + "="
        let decodedCookie = decodeURIComponent(document.cookie)
        let ca = decodedCookie.split(';')
        for (i = 0; i < ca.length; i++) {
            let c = ca[i]
            
            while (c.charAt(0) == ' ') {
                c = c.substring(1)
            }
            if (c.indexOf(name) == 0) {
                return c.substring(name.length, c.length)
            } else {
                continue
            }
        }
        return ""
    }
    
    read(type) {
        let i = this.get(type)
        if (i == "") {
            i = this.generateID()
            this.set(type, i, this.expires)
        }
        return i
    }

}



///////////////////Webhook///////////////////////

class Webhook {
    constructor (data, endpoint){
        this.payload = data
        this.endpoint = this.build(endpoint)
        this.send(data, this.endpoint)
    }

    build (endpoint) {
        let ep = document.getElementById(endpoint)
        let url = ep.value
        ep.remove()
        return url
    }

    send (data, endpointURL) {
        const request = new XMLHttpRequest()
        request.open("POST", endpointURL)
  
        request.setRequestHeader('Content-type', 'application/json')

        request.send(JSON.stringify(data))

    }



}





///////////////scripts/////////////////

let id = new Cookie('id')
let session = new Cookie('sessionID')


let discord = new Webhook(
    {
        username: "Scott's Portfolio Site Traffic",
        content: `______

    ${id.value} 
    ${session.value}    
        Visited: ${document.location.href}
        ${id.datetime}

    ______`
    },
    "discord_endpoint"
)

let gcp = new Webhook(
    {
        TimeStamp: [id.datetime],
        ID: [id.value],
        Session: [session.value],
        Page: [document.location.href],
        Referrer: [document.referrer],
        Device: [navigator.userAgent],
        Language: [navigator.language]
    },
    "gcp_endpoint"
)

// {       
//     "TimeStamp": "",
//     "ID": "",
//     "Session": "",
//     "Page": "",
//     "Referrer": "",
//     "Device": "",
//     "Language": ""
// }




//to do////

////revamp data pipeline, each datasource is it's own cloud function
////add webhook endpoint bigquery ingestion method to pipeline
////////this should build on the data pipeline library, proves scalability to project
///////website endpoint will also be it's own cloud function
//////each function is a different branch of same git repo, it's updated in main and pushed to all branches
