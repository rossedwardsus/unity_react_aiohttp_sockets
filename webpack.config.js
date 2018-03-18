module.exports = {
  entry: __dirname + '/public/js/app.js',
  output: {
    path: __dirname + "/public/js",
    filename: 'build.js'
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
          options: {
              presets: ['env', 'react']
          }
        }
      }
    ]
  }
};