const webpack = require('webpack');
const config = {
    entry:  [__dirname + '/src/assets/scripts/index.js'],
    output: {
        path: __dirname + '/src/',
        filename: 'static/js/bundle.js',
    },
    resolve: {
        extensions: ['.js']
    },
    module: {
        loaders: [
            {
                test: /\.js?/,
                exclude: /node_modules/,
                use: 'babel-loader'
            }
        ]
    }
};
module.exports = config;