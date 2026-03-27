import { useState, useCallback } from "react";

export function useAIStream() {
  const [output, setOutput] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const streamChat = useCallback(async (messages) => {
    setLoading(true);
    setOutput("");
    setError(null);

    try {
      const apiUrl = `${import.meta.env.VITE_API_BASE_URL}/api/v1/ai/stream`;
      console.log("[v0] Fetching from:", apiUrl);

      const response = await fetch(apiUrl, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ messages }),
      });

      if (!response.ok) {
        throw new Error(`API error: ${response.status} ${response.statusText}`);
      }

      if (!response.body) {
        throw new Error("Response body is empty");
      }

      const reader = response.body.getReader();
      const decoder = new TextDecoder();

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        const chunk = decoder.decode(value);
        setOutput((prev) => prev + chunk);
      }
    } catch (err) {
      const errorMsg = err instanceof Error ? err.message : "Unknown error occurred";
      console.error("[v0] Stream error:", errorMsg);
      setError(errorMsg);
      setOutput(`Error: ${errorMsg}`);
    } finally {
      setLoading(false);
    }
  }, []);

  return { output, loading, error, streamChat };
}
