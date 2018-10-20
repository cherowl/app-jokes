import * as types from '../constants/actions';

const initialState = {
  authenticated: false,
  authenticationError: '',
};

const auth = (state = initialState, action = {}) => {
  switch (action.type) {
    case types.SET_AUTHENTICATION_ERROR: {
      const authenticationError = action.error;
      return { ...state, authenticationError };
    }
    case types.SET_AUTHENTICATED_STATUS: {
      const authenticated = action.status;
      return { ...state, authenticated };
    }
    default:
      return state;
  }
};

export default auth;
