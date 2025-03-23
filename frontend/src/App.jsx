import { useState } from "react";
import axios from "axios";
import './styles.css';


function App() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [file, setFile] = useState(null);

  const handleUpload = async () => {
    if (!file) return alert("Please select a PDF");
    const formData = new FormData();
    formData.append("file", file);

    try {
      await axios.post("http://127.0.0.1:8000/api/upload_pdf", formData);
      alert("PDF uploaded and indexed!");
    } catch (error) {
      console.error("Upload error:", error);
    }
  };

  const handleSearch = async () => {
    if (!query) return;
    setLoading(true);
    try {
      const response = await axios.get("http://127.0.0.1:8000/api/search", {
        params: { query, top_k: 5 },
      });
      setResults(response.data.results);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
    setLoading(false);
  };

  return (
    <div className="container">
      <h1>PDF Search</h1>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Upload PDF</button>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Enter your query..."
      />
      <button onClick={handleSearch} disabled={loading}>
        {loading ? "Searching..." : "Search"}
      </button>
      <div className="results">
        {results.map((res, index) => (
          <div key={index} className="result">
            <p><strong>Chunk:</strong> {res.chunk}</p>
            <p><strong>Score:</strong> {res.score.toFixed(4)}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;


