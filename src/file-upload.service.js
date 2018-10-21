import * as axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8081';

function upload(formData) {
    const url = `${BASE_URL}/uploads/data`;
    return axios.post(url, formData)
}

export { upload }
