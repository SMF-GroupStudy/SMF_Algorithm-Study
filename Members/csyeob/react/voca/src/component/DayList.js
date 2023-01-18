import dummy from "../db/data.json"
export default function DayList(){
    console.log(dummy);
    return<ul className="list_day">
        {dummy.days.map(day =>(
            <li key = {day.id}>
                Day {day.day}
            </li>
        ))}
            {/*반복문을 사용할 것인데, 이때는 map을 사용하는게 좋음
               map은 배열을 받아서 배열로 내보냄.
            */}
    </ul>;
}