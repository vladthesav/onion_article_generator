import Button from './Button'
import React, { useState } from 'react';

const TextView = ({title}) => {
    const [input, setInput] = useState('Florida man');
    const [output, setOutput] = useState('')

    const apiRequest = (e) => {
        const endpoint = '/predict'
        
        const options = {
            method: "POST",
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            credentials: "include",
            body: JSON.stringify({text:input}),
          };
          
        fetch(endpoint, options)
        .then((response) => response.json())
        .then((data) =>setOutput(data.output));

    }

    return (
        <div>
            <form>
                <label>
                    <input type="text" name="input" 
                    onChange={e => setInput(e.target.value)} 
                    placeholder="Florida man"/>
                </label>
            </form>
            <p>{output}</p>
            <div><Button color='rgb(0, 107, 58)' text = 'complete' onClick = {apiRequest}/></div>
        </div>
        
    
    )
}

export default TextView