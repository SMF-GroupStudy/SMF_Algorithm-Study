import {Link} from "react-router-dom"
import { useEffect, useInsertionEffect, useState } from 'react';
import useFetch from './../hooks/useFetch';

export default function DayList(){
    const days = useFetch("http://localhost:3002/days");

    // const [days, setDays] = useState([]);
    
    // useEffect(()=>{
    //     fetch("http://localhost:3002/days")
    //     .then(res =>{
    //         return res.json();
    //     })
    //     .then(data =>{
    //         setDays(data);
    //     })
    // },[]);

    return<ul className="list_day">
        {days.map(day =>(
            <li key = {day.id}>
                <Link to ={`/day/${day.day}`}>Day {day.day}</Link>
            </li>
        ))}
            {/*반복문을 사용할 것인데, 이때는 map을 사용하는게 좋음
               map은 배열을 받아서 배열로 내보냄.

               html에서는 a href를 사용하지만 리액트 라우터에서는
               Link to를 사용
            */}
    </ul>;
}