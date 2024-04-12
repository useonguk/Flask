import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [professorTimetable, setProfessorTimetable] = useState([]);
  const [studentTimetable, setStudentTimetable] = useState([
    {
      course_name: "Mathematics",
      credit: 3,
      day: "Monday",
      start_time: "09:00",
    },
    {
      course_name: "Mathematics",
      credit: 3,
      day: "\ud654\uc694\uc77c",
      start_time: "09:00",
    },
  ]);

  useEffect(() => {
    fetchProfessorTimetable();
    fetchStudentTimetable();
  }, []);

  const fetchProfessorTimetable = async () => {
    try {
      const response = await axios.get(
        "http://127.0.0.1:5000/api/professor/time-table/1"
      );
      console.log(response.data.lectures);
      setProfessorTimetable(response.data.lectures || []);
    } catch (error) {
      console.error("Error fetching professor timetable:", error);
    }
  };

  const fetchStudentTimetable = async () => {
    try {
      const response = await axios.get(
        "http://127.0.0.1:5000/api/student/time-table/1"
      );
      console.log(response.data.lectures);
      setStudentTimetable(response.data.lectures || []);
    } catch (error) {
      console.error("Error fetching student timetable:", error);
    }
  };

  const generateTimetable = (data) => {
    let timetable = {};

    data.forEach((course) => {
      let startHour = parseInt(course.start_time.split("시")[0]);
      let endHour = startHour + parseInt(course.credit);

      for (let i = startHour; i < endHour; i++) {
        if (!timetable[course.day]) {
          timetable[course.day] = {};
        }
        if (!timetable[course.day][i]) {
          timetable[course.day][i] = [];
        }
        timetable[course.day][i].push(course.course_name);
      }
    });

    return timetable;
  };

  const displayTimetable = (timetable) => {
    return (
      <div className="table-container">
        <table className="timetable-table">
          <thead>
            <tr>
              <th>Time</th>
              <th>Monday</th>
              <th>Tuesday</th>
              <th>Wednesday</th>
              <th>Thursday</th>
              <th>Friday</th>
              <th>Saturday</th>
              <th>Sunday</th>
            </tr>
          </thead>
          <tbody>
            {[9, 10, 11, 12, 13, 14, 15, 16, 17, 18].map((hour) => (
              <tr key={hour}>
                <td>
                  {hour}:00 - {hour + 1}:00
                </td>
                {[
                  "Monday",
                  "Tuesday",
                  "Wednesday",
                  "Thursday",
                  "Friday",
                  "Saturday",
                  "Sunday",
                ].map((day) => (
                  <td key={day}>
                    {timetable[day] &&
                      timetable[day][hour] &&
                      timetable[day][hour].map((course) => (
                        <div key={course}>{course}</div>
                      ))}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  };

  return (
    <div className="App">
      <h1>Professor's Time Table</h1>
      {displayTimetable(professorTimetable)}
      <h1>Student's Time Table</h1>
      {displayTimetable(generateTimetable(studentTimetable))}
    </div>
  );
}

export default App;
