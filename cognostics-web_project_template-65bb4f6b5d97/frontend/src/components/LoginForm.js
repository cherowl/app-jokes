import React from 'react';
import PropTypes from 'prop-types';

export default class LoginForm extends React.Component {
  componentDidMount() {
    this.username = '';
    this.password = '';
  }

  handleUsernameChange = (event) => {
    this.username = event.target.value;
  };

  handlePasswordChange = (event) => {
    this.password = event.target.value;
  };

  login = () => {
    this.props.login(this.username, this.password);
  };

  render() {
    return (
      <div>
        <input type="text" required placeholder="username" onChange={this.handleUsernameChange} />
        <input type="password" required placeholder="password" onChange={this.handlePasswordChange} />
        <button onClick={this.login}>{'Login'}</button>

        <div>{this.props.error}</div>
      </div>
    );
  }
}

LoginForm.propTypes = {
  error: PropTypes.string,
  login: PropTypes.func.isRequired,
};
LoginForm.defaultProps = {
  error: '',
};
