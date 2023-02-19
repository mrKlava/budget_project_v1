import React, {useState} from 'react'
import httpClient from '../httpClient'

function RegisterPage() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')

  const handelClick = async (e) => {
    e.preventDefault()
    
    try {
      const resp = await httpClient.post("//localhost:5000/register", {
        email,
        password
      })

      if (resp.status === 200) window.location.href = '/' 
    } catch(error) {
      if (error.response.status === 401) console.log(error.response.data) 
      setEmail('')
      setPassword('')
    }
  }
  return (
    <div>
      <h1>Register</h1>
       <form>
        <input 
          type="email" 
          name='email' 
          placeholder='Email'
          value={email}
          onChange={(e)=> setEmail(e.target.value)}
        />
        <input 
          type="password" 
          name='password' 
          placeholder='Password'
          value={password}
          onChange={(e)=> setPassword(e.target.value)}
        />
        
        <button onClick={handelClick}>Register</button>
      </form>
    </div>
  )
}

export default RegisterPage