export interface HealthResponse {
    status: string;
    message: string;
  }
  
  import { apiClient } from "./client";
  
  export const fetchHealth = async (): Promise<HealthResponse> => {
    const res = await apiClient.get("/api/v1/health");
    return res.data;
  };