import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [resumes, setResumes] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8000/get_resumes/").then((res) => {
      setResumes(res.data);
    });
  }, []);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);

    await axios.post("http://localhost:8000/upload_resume/", formData);
    alert("Resume uploaded!");
  };

  return (
    <div className="container">
      <h1>Resume Parser</h1>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Upload Resume</button>

      <h2>Past Resumes</h2>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Phone</th>
          </tr>
        </thead>
        <tbody>
          {resumes.map((resume, index) => (
            <tr key={index}>
              <td>{resume.name}</td>
              <td>{resume.email}</td>
              <td>{resume.phone}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
