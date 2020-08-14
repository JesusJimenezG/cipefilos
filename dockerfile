FROM alpine:3.11

ENV NODE_VERSION 14.8.0

ENV NPM_CONFIG_LOGLEVEL info
# make the 'app' folder the current working directory
WORKDIR /app/

# copy package.json to the /app/ folder
COPY package.json ./

# https://docs.npmjs.com/cli/cache
RUN npm cache verify

# install project dependencies
RUN npm install

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# expose port 8080 to the host
EXPOSE 8080

# run the development server
CMD ["npm", "run", "serve"]
