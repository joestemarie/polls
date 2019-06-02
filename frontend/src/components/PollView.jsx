import  React, { Component } from  'react';
import PollsService from "./PollsService.jsx";
import Plot from "react-plotly.js";

const pollService = new PollsService();

class PollView extends Component {
  constructor(props) {
    super(props);
    this.state = {
      poll: "",
      questions: ""
    }
  }

  componentDidMount() {
    let this_pk = this.props.match.params.pk;
    pollService.getPoll(this_pk).then((poll) => {
      this.setState(() => ({ poll }))
    });
    pollService.getPollQuestions(this_pk).then((questions) => {
      this.setState(() => ({ questions }))
    });
  }

  plotlyDataFormat(json_data_string) {
    const json_data = JSON.parse(json_data_string);
    const plotly_data = [{
      y: json_data.map(a => a.answer),
      x: json_data.map(a => a.pct),
      type: "bar",
      orientation: "h",
      marker: {
        color: "#F24B3B"
      }
    }];
    return(plotly_data)
  }

  render() {
    return (
      <div>
        <div className="row poll-view">
          <div className="col">
            <h1>{this.state.poll.pollster_name}</h1>
            <p>{this.state.poll.field_date_start} - {this.state.poll.field_date_end}</p>
            <p>{this.state.poll.n_size} {this.state.poll.sample}</p>
          </div>
        </div>

        {Array.from(this.state.questions).map( q =>
          <div className="row poll-view" key={q.id}>
            <h3>
              {q.candidate ? q.question_text + ": " + q.candidate_name : q.question_text}
            </h3>

            <Plot
              data={this.plotlyDataFormat(q.data_json)}
              layout={{height: 400}}
            />
          </div>
        )}

      </div>
    );
  }
}

export default PollView;
