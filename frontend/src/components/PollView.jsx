import  React, { Component } from  'react';
import PollsService from "./PollsService.jsx";

const pollService = new PollsService();

class PollView extends Component {
  constructor(props) {
    super(props);
    this.state = {
      poll: ""
    }
  }

  componentDidMount() {
    pollService.getPoll(this.props.match.params.pk).then((poll) => {
      this.setState(() => ({ poll }))
    });
  }

  render() {
    return (
      <div>
        <h1>{this.state.poll.pollster_name}</h1>
      </div>
    );
  }
}

export default PollView;
