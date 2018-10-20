import { dispatch } from './ReduxService';
import { broadcastMessageUpdate, receiveResponse, sendRequest } from '../actions/APIServiceActions';

class APIService {
  constructor() {
    this.socket = null;
    this.lastRequestId = 0;
  }

  init = (socket) => {
    this.socket = socket;
    this.socket.on('response', (data) => {
      dispatch(receiveResponse(data));
    });
    this.socket.on('broadcast_example', (data) => {
      console.log(data);
      dispatch(broadcastMessageUpdate(data));
    });
  };

  destroy = () => {
    this.socket = null;
  };

  sendRequest = (type, data) => {
    if (this.socket !== null) {
      this.lastRequestId += 1;
      const request = { id: this.lastRequestId, type, data };
      this.socket.emit('request', request);
      dispatch(sendRequest(request));
    } else {
      console.error('APIService: Socket is not initialized');
    }
  };
}

export default new APIService();
