FROM node:13.12.0-alpine
WORKDIR /app/frontend
ENV NODE_ENV development

COPY package.json ./
RUN npm install -q
RUN npm install react-scripts@5.0.1 -g 
ENV CHOKIDAR_USEPOLLING=true
COPY . ./
EXPOSE 3000
CMD ["npm", "start"]
