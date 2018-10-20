import React from 'react';
import { connect } from 'react-redux';
import { withRouter } from 'react-router';
import LoginForm from '../components/LoginForm';
import AuthService from '../services/AuthService';

class LoginFormContainer extends React.Component {
  componentWillReceiveProps(nextProps) {
    this.authenticationCheck(nextProps);
  }

  authenticationCheck = (props) => {
    const { state, history, location } = props;
    if (state.authenticated) {
      const { from } = location.state || { from: { pathname: '/' } };
      history.replace(from);
    }
  };

  render() {
    const { state } = this.props;
    return (
      <LoginForm
        login={AuthService.login}
        error={state.authenticationError}
      />
    );
  }
}

const mapStateToProps = state => ({
  state: state.auth,
});

export default withRouter(connect(mapStateToProps)(LoginFormContainer));
