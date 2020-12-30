export default class DataApi {
    static async getState() {
        return await this._fetchState()
    }

    static _fetchState() {
        return fetch("http://localhost:5000/state").then((res) => {
            if (res.ok) {
                return res.text()
            }
            alert("Error")
        }).then(data => {
            let parsed_data = JSON.parse(data)
            let humid = parsed_data.humid;
            let humidity = parsed_data.humidity
            let temperature = parsed_data.temperature
            let luminity = parsed_data.lightness
            return { humid, humidity, temperature, luminity }
        })
    }

    static async fetchJSONUrl(url) {
        return await this._fetchUrl(url)
    }

    static _fetchUrl(url) {
        return fetch(url).then((res) => {
            if (res.ok) {
                return res.text()
            }
            alert("Error")
        }).then(data => {
            let parsed_data = JSON.parse(data)

            return parsed_data
        })
    }
}