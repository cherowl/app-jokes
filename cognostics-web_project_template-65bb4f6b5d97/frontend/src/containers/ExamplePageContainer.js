import React from 'react';
import { connect } from 'react-redux';
import ExampleComponent from '../components/ExampleComponent';
import APIService from '../services/APIService';

class ExampleComponentContainer extends React.Component {
  getFullName = () => {
    APIService.sendRequest('work_for_ten_seconds');
    APIService.sendRequest('get_user_full_name');
  };

  render() {
    const { fullName, broadcastMessage } = this.props.exampleStore;
    return (
      <ExampleComponent
        fullName={fullName}
        getFullName={this.getFullName}
        broadcastMessage={broadcastMessage}
      />
    );
  }
}

const mapStateToProps = state => ({
  exampleStore: state.example,
});

export default connect(mapStateToProps)(ExampleComponentContainer);
