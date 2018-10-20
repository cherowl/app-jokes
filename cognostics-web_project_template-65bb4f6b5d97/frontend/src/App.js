import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { Provider } from 'react-redux';
import AppPage from './pages/AppPage';
import LoginPage from './pages/LoginPage';
import ReduxService from './services/ReduxService';

const App = () => (
  <Provider store={ReduxService.store}>
    <BrowserRouter>
      <Switch>
        <Route exact path="/login" component={LoginPage} />
        <Route path="/" component={AppPage} />
      </Switch>
    </BrowserRouter>
  </Provider>
);

export default App;
