import io from 'socket.io-client';
import APIService from './APIService';
import { setAuthenticatedStatus, setAuthenticationError } from '../actions/authActions';
import { dispatch } from '../services/ReduxService';

class AuthService {
  constructor() {
    this.socket = null;
  }

  login = (username, password) => {
    const request = new XMLHttpRequest();
    request.open('POST', 'http://localhost:8000/auth/login', true);
    request.timeout = 5000; // 5s timeout
    request.withCredentials = true;
    request.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

    request.ontimeout = () => {
      dispatch(setAuthenticationError('Timeout connecting to the backend'));
    };

    request.onreadystatechange = () => {
      if (request.readyState === 4) {
        if (request.status === 200) {
          this.connect();
        } else {
          switch (request.status) {
            case -1:
            case 0:
            case 404:
            case 500:
              dispatch(setAuthenticationError('Service not available'));
              break;

            case 403:
              dispatch(setAuthenticationError(request.responseText));
              break;

            default:
              dispatch(setAuthenticationError(`${request.status}: ${request.statusText}`));
          }
        }
      }
    };
    request.send(`username=${username}&password=${password}`);
  };

  connect = () => new Promise((resolve) => {
    this.socket = io.connect('http://localhost:8000', {
      transports: ['websocket'],
      randomizationFactor: 0,
      secure: true,
    });

    this.socket.on('connect', () => {
      this.signIn();
      resolve();
    });

    this.socket.on('connect_error', () => {
      this.signOut();
      resolve();
    });
  });

  signIn = () => {
    APIService.init(this.socket);
    dispatch(setAuthenticatedStatus(true));
  };

  signOut = () => {
    APIService.destroy();
    dispatch(setAuthenticatedStatus(false));
    if (this.socket !== null) {
      this.socket.disconnect();
      this.socket = null;
    }
  };
}

export default new AuthService();
