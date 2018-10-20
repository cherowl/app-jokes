import * as types from '../constants/actions';

export const setAuthenticationError = error => ({
  type: types.SET_AUTHENTICATION_ERROR,
  error,
});

export const setAuthenticatedStatus = status => ({
  type: types.SET_AUTHENTICATED_STATUS,
  status,
});
