import { useHealth } from "../hooks/useHealth";

export const Home = () => {
    const { data, isLoading, error } = useHealth();


  return (
    <div className="p-16 font-sans flex flex-col items-center justify-center">
      <h1 className="text-4xl font-bold">♟️ ChessInsight</h1>
      {isLoading && <p className="text-lg">Checking backend...</p>}
      {error && <p className="text-red-500">Backend error</p>}
      {data && <p className="text-lg">Backend status: <span className="font-bold text-green-500">{data.status}</span></p>}
    </div>
  );
};
