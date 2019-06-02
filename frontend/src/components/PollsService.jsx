import axios from "axios";
const API_URL = "http://localhost:8000";

export default class PollsService {
  constructor() {}

  getPolls() {
    const url = `${API_URL}/api/polls/`;
    return axios.get(url).then(res => res.data);
  }

  getPoll(pk) {
    const url = `${API_URL}/api/polls/${pk}/`;
    return axios.get(url).then(res => res.data);
  }

  getPollQuestions(pk) {
    const url = `${API_URL}/api/polls/${pk}/question_result/`;
    return axios.get(url, {params: {poll_id: pk}}).then(res => res.data);
  }
}
