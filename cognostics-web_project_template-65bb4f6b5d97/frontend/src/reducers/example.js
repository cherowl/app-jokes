import * as types from '../constants/actions';

const initialState = {
  broadcastMessage: '',
  fullName: '',
};

const handleResponse = (response) => {
  switch (response.type) {
    case 'get_user_full_name': {
      return { fullName: response.data };
    }
    default:
      return {};
  }
};

const example = (state = initialState, action = {}) => {
  switch (action.type) {
    case types.BROADCAST_MESSAGE_UPDATE: {
      return { ...state, broadcastMessage: action.message };
    }
    case types.RECEIVE_RESPONSE: {
      return { ...state, ...handleResponse(action.response) };
    }
    default:
      return state;
  }
};

export default example;
