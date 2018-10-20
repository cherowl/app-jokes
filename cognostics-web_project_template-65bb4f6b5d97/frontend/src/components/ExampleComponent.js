import React from 'react';

const ExampleComponent = (props) => (
  <div>
    <div>
      <button onClick={props.getFullName}>{'Get full name'}</button>
      {`My full name: ${props.fullName}`}</div>
    <div>{`Broadcast message: ${props.broadcastMessage}`}</div>
  </div>
);

export default ExampleComponent;
