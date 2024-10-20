import React from 'react'
import './Chats.css'
import profile from '../../Assets/profile.png'

const Chats = () => {
    //   chats

const chats = [
    {
      image:profile,
      name: 'John Doe',
      message: 'Please did you understand what was explained ...',
    },
    {
      name: 'John Doe',
      message: 'Please did you understand what was explained ...',
    },
  ];
  return (
    <>
  {/* chat */}

<div className="chat-list">
      <h2>Chats</h2>
      <div className="chat-items">
        {chats.map((chat, index) => (
          <div className="chat-item" key={index}>
            <div className="chat-info" style={{display:'flex',gap:'1rem'}}>
           <img src={chat.image} alt="" className='chat-img'/>
           <div>
              <strong>{chat.name}</strong>
              <p>{chat.message}</p>
              </div>
            </div>
          </div>
        ))}
      </div>
      <a href="#" className="see-all">See all</a>
    </div>
    </>
  )
}

export default Chats