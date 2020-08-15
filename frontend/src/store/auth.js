import axios from 'axios';

const ENDPOINT_PATH = 'http://localhost:8000/auth/';

export default {
  register(username, email, password1, password2) {
    const user = {
      username, email, password1, password2,
    };
    return axios.post(`${ENDPOINT_PATH}registration/`, user);
  },
};
