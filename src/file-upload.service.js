import * as axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8080';

function upload(formData) {
    const url = `${BASE_URL}/files/upload`;
    return axios.post(url, formData)
        /*// get data
        .then(x => x.data)
        // add url field
        .then(x => x.map(img => Object.assign({},
            img, { url: `${BASE_URL}/uploads/${img.id}` })));*/
}

export { upload }
