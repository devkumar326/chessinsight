import axios from "axios";

const API_BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export const testStockfish = async (): Promise<{ result: string }> => {
  const response = await axios.get(`${API_BASE_URL}/api/v1/stockfish`);
  return response.data;
};