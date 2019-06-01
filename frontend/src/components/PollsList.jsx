import  React, { Component } from  'react';
import PollsService from "./PollsService.jsx";

const pollService = new PollsService();

class PollsList extends Component {
  constructor(props) {
    super(props);
    this.state = {
      polls: []
    };
  }

  componentDidMount() {
    var self = this;
    pollService.getPolls().then(function(result) {
      console.log(result);
      self.setState({ polls: result })
    });
  }

  render() {
    console.log(pollService.getPolls());
    return (
      <div className="polls-list">
        <div className="row">
          {this.state.polls.map( poll =>
            <div className="col-sm-4" key={poll.id}>
              <div className="card">
                <div className="card-body">
                  <h5 className="card-title">{poll.pollster_name}</h5>
                  <h6 className="card-subtitle mb-2 text-muted">{poll.field_date_start} - {poll.field_date_end}</h6>
                  <a href="#" className="card-link">Details</a>
                </div>
              </div>
            </div>
          )}
        </div>
      </div>
    );
  }
}

export default PollsList;
