import React from 'react';
import { connect } from 'react-redux';
import { withRouter } from 'react-router';
import { Route, Switch } from 'react-router-dom';
import ExamplePage from '../pages/ExamplePage';

class AppPageContainer extends React.Component {
  componentWillMount() {
    this.authenticationCheck(this.props);
  }

  authenticationCheck = (props) => {
    const { auth, history, location } = props;
    if (!auth.authenticated) {
      history.replace({
        pathname: '/login',
        state: { from: location },
      });
    }
  };

  render() {
    return (
      <Switch>
        <Route exact path={'/'} component={ExamplePage} />
        <Route render={() => <div>{'404 Not Found'}</div>} />
      </Switch>
    );
  }
}

const mapStateToProps = store => ({
  auth: store.auth,
});

export default withRouter(connect(mapStateToProps)(AppPageContainer));
