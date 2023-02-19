import React from 'react'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import LandingPage from './pages/LandingPage'
import LoginPage from './pages/LoginPage'
import NotFound from './pages/NotFound'
import RegisterPage from './pages/RegisterPage'


function Router() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='*' element={<NotFound/>} />
        <Route path='/' element={<LandingPage/>} />
        <Route path='/login' element={<LoginPage/>} />
        <Route path='/register' element={<RegisterPage/>} />
      </Routes>
    </BrowserRouter>
  )
}

export default Router