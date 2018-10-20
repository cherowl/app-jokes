import * as types from '../constants/actions';

export const sendRequest = request => ({
  type: types.SEND_REQUEST,
  request,
});

export const receiveResponse = response => ({
  type: types.RECEIVE_RESPONSE,
  response,
});

export const broadcastMessageUpdate = message => ({
  type: types.BROADCAST_MESSAGE_UPDATE,
  message,
});
