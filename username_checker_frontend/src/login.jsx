import React from 'react'

function Login() {
  function handleOnChange(){
    console.log('garvit')
  }

  return (
    <div className='login'>
    <input type="text" placeholder='Enter Username' onChange={(e)=>{handleOnChange()}} />
    <input type="text" placeholder='Enter Password' />
    <button>Login</button>
    </div>
  )
}

export default Login
