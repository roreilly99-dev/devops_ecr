# First stage: build
FROM node:18 AS builder

WORKDIR /app

# Only copy the package files first for layer caching
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the app
COPY . .

# Build the app
RUN npm run build

# Second stage: production image
FROM node:18-alpine AS runner

WORKDIR /app

# Only copy what is needed for production
COPY --from=builder /app/public ./public
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json

EXPOSE 3000

CMD ["npm", "start"]
