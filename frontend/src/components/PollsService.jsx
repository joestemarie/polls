import axios from "axios";
const API_URL = "http://localhost:8000";

export default class PollsService {
  constructor() {}

  getPolls() {
    const url = `${API_URL}/api/polls/`;
    return axios.get(url).then(res => res.data);
  }
}
