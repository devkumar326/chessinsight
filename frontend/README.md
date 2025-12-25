# ChessInsight Frontend

The frontend application for ChessInsight, a modern chess analysis platform built with React and TypeScript.

## Tech Stack

- **Framework**: React 19
- **Language**: TypeScript
- **Build Tool**: Vite 7
- **Styling**: TailwindCSS 4
- **State Management**: TanStack React Query
- **HTTP Client**: Axios
- **Routing**: React Router DOM v7
- **Linting**: ESLint

## Project Structure

```
frontend/
├── public/              # Static assets
│   └── vite.svg
├── src/
│   ├── api/            # API client and service functions
│   │   ├── client.ts   # Axios instance configuration
│   │   ├── health.ts   # Health check API calls
│   │   └── stockfish.ts
│   ├── assets/         # Images, icons, etc.
│   ├── hooks/          # Custom React hooks
│   │   └── useHealth.ts
│   ├── pages/          # Page components
│   │   └── Home.tsx
│   ├── App.tsx         # Root application component
│   ├── App.css         # Application styles
│   ├── main.tsx        # Application entry point
│   └── index.css       # Global styles
├── eslint.config.js    # ESLint configuration
├── tsconfig.json       # TypeScript configuration
├── vite.config.ts      # Vite configuration
├── Dockerfile          # Docker configuration
└── package.json        # Dependencies and scripts
```

## Prerequisites

- Node.js 18.x or higher
- npm or yarn package manager
- Docker (optional, for containerized deployment)

## Installation

### Local Development

1. **Navigate to the frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

### Docker Development

Build and run the frontend container:
```bash
docker build -t chessinsight-frontend .
docker run -p 5173:5173 chessinsight-frontend
```

Or use docker-compose from the project root:
```bash
cd ..
docker-compose up frontend
```

## Running the Application

### Development Server

Start the development server with hot-reload:
```bash
npm run dev
```

The application will be available at http://localhost:5173

### Production Build

Build the application for production:
```bash
npm run build
```

Preview the production build:
```bash
npm run preview
```

## Available Scripts

- `npm run dev` - Start development server with hot-reload
- `npm run build` - Build for production
- `npm run preview` - Preview production build locally
- `npm run lint` - Run ESLint to check code quality

## Environment Variables

Create a `.env` file in the frontend directory:

```env
VITE_API_BASE_URL=http://localhost:8000
```

### Accessing Environment Variables

In your code:
```typescript
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;
```

## Features

- ⚡ **Lightning Fast**: Powered by Vite for instant HMR
- 🎨 **Modern UI**: Styled with TailwindCSS 4
- 📱 **Responsive Design**: Works on all device sizes
- 🔄 **Smart Data Fetching**: TanStack React Query for caching and state management
- 🛣️ **Routing**: React Router for navigation
- 📦 **Type Safety**: Full TypeScript support
- 🎯 **Code Quality**: ESLint configured for React and TypeScript

## API Integration

The frontend communicates with the backend API through Axios. The API client is configured in `src/api/client.ts`:

```typescript
import axios from 'axios';

const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000',
});

export default apiClient;
```

## Development Guidelines

### Adding New Pages

1. Create a new component in `src/pages/`
2. Add routing in `App.tsx` or create a router configuration
3. Create API service functions in `src/api/` if needed
4. Create custom hooks in `src/hooks/` for complex logic

### Component Structure

```typescript
import React from 'react';

interface ComponentProps {
  // Define your props
}

export const ComponentName: React.FC<ComponentProps> = ({ props }) => {
  return (
    <div>
      {/* Your component JSX */}
    </div>
  );
};
```

### Using React Query

```typescript
import { useQuery } from '@tanstack/react-query';
import { getHealthStatus } from '../api/health';

export const useHealth = () => {
  return useQuery({
    queryKey: ['health'],
    queryFn: getHealthStatus,
  });
};
```

## Styling with TailwindCSS

TailwindCSS 4 is configured and ready to use. Simply add utility classes to your components:

```tsx
<div className="flex items-center justify-center h-screen bg-gray-100">
  <h1 className="text-4xl font-bold text-blue-600">ChessInsight</h1>
</div>
```

## Code Quality

### Linting

Run ESLint to check for code issues:
```bash
npm run lint
```

ESLint is configured for:
- React hooks rules
- React refresh rules
- TypeScript best practices

### Type Checking

TypeScript will check types during build and in your IDE. Run type checking manually:
```bash
npx tsc --noEmit
```

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Performance Optimization

- Code splitting with React Router
- Lazy loading of components
- Optimized bundle size with Vite
- React Query for intelligent data caching

## Troubleshooting

### Port Already in Use

If port 5173 is already in use, you can specify a different port:
```bash
npm run dev -- --port 3000
```

### API Connection Issues

Ensure the backend is running and the `VITE_API_BASE_URL` environment variable is correctly set.

## License

MIT

## Support

For issues and questions, please open an issue in the repository.
