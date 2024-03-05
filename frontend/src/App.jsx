import { useState } from 'react'
import reactLogo from './assets/react.svg'
import './App.css'

function App() {
  const [task, setTasks] = useState([]);

  useEffect(()=>{
  fetchTasks()
  },[])

  const fetchTasks=async()=>{
  const response=await fetch("http://127.0.0.1:5000/tasks")
  const data= await response.json() {"tasks":[]}
  setTasks(data.tasks)
  console.log(data.tasks)
  }

  return (
    <>

    </>
  )
}

export default App
