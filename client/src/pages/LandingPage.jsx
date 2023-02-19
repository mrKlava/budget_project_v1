import React, { useState, useEffect } from 'react'
import httpClient from '../httpClient'

function LandingPage() {
  const [user, setUser] = useState(null)

  const handleClick = async () => {
    const resp = await httpClient.post("//localhost:5000/logout")
    window.location.href = '/'
  }

  useEffect(() => {
    (async () => {

      try {
        const resp = await httpClient.get("//localhost:5000/@me")
        setUser(resp.data)
      } catch (error) {
        console.log("Not logged")
      }
    })()
  }, [])

  return (
    <div>
      <h1>Landing Page</h1>
      {user
        ? (
          <div>
            <p>Welcome {user.email}</p>
            <button onClick={handleClick}>Log out</button>
          </div>
        )
        : (
          <div>
            <p>You are not logged in</p>
            <a href='/login'>
              <button>Log in</button>
            </a>
            <a href='/register'>
              <button>Register</button>
            </a>
          </div >
        )}


    </div >
  )
}

export default LandingPage