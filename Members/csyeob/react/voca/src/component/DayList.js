import dummy from "../db/data.json"
import {Link} from "react-router-dom"
export default function DayList(){
    return<ul className="list_day">
        {dummy.days.map(day =>(
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