import React, { useEffect, useState } from "react";

export default function EventsList() {

    const [events, setEvents] = useState([]);

    useEffect(() => {
        fetch("http://localhost:5000/api/events")
            .then(res => res.json())
            .then(data => setEvents(data))
            .catch(() => setEvents([]));
    }, []);

    return (
        <div>
            <h2>Upcoming Campus Events</h2>
            {events.length === 0 ? (
                <p>No events available.</p>
            ) : (
                <ul>
                    {events.map(ev => (
                        <li key={ev.id}>
                            <strong>{ev.title}</strong> – {ev.date}
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
}