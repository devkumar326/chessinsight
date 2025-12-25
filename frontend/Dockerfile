FROM node:20-alpine

WORKDIR /app

# Install deps first (better caching)
COPY package.json package-lock.json ./
RUN npm install

# Copy rest of the app
COPY . .

# Vite default port
EXPOSE 5173

# Run Vite dev server
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]

