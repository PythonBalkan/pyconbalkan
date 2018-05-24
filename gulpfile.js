let gulp = require('gulp');
let sass = require('gulp-sass');
let sourcemaps = require('gulp-sourcemaps');
let postcss = require('gulp-postcss');
let babel = require('gulp-babel');
let concat = require('gulp-concat');
let uglify = require('gulp-uglify');
let imagemin = require('gulp-imagemin');
let livereload = require('gulp-livereload');

let exec = require('child_process').exec;
let autoprefixer = require('autoprefixer');
let cssnano = require('cssnano');

let srcPath = 'pyconbalkan/core/static/src';
let dstPath = 'pyconbalkan/core/static/dst';

// CSS assets
//
// The SASS files are run through postcss/autoprefixer and placed into one 
// single main styles.min.css file (and sourcemap)

gulp.task('css', function () {
    let processors = [
        autoprefixer,
        cssnano
    ];
    return gulp.src(`${srcPath}/sass/main.scss`)
        .pipe(sourcemaps.init())
        .pipe(sass({
            includePaths: [
                'node_modules/'
            ]
        }).on('error', sass.logError))
        .pipe(postcss(processors))
        .pipe(concat('app.min.css'))
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest(`${dstPath}/css/`))
        .pipe(livereload());
});

// Javascript assets
//
// All regular .js files are collected, minified and concatonated into one
// single main.min.js file (and sourcemap)

gulp.task('js', ['vendor'], function () {
    return gulp.src(`${srcPath}/js/app.js`)
        .pipe(sourcemaps.init())
        .pipe(babel({
            presets: ['es2015']
        }))
        .pipe(concat('app.min.js'))
        .pipe(uglify())
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest(`${dstPath}/js/`))
        .pipe(livereload());
});

// External Javascript assets
//
// Any required external libraries are collected, minified and concatonated 
// into one single vendor.min.js file (and sourcemap)

gulp.task('vendor', function () {
    return gulp.src([
        'node_modules/jquery/dist/jquery.js',
    ])
    .pipe(concat('vendor.min.js'))
    .pipe(uglify())
    .pipe(gulp.dest(`${dstPath}/js/`));
});

gulp.task('imgCompression', function () {
    return gulp.src(`${srcPath}/images/*`)
    .pipe(imagemin()) // Compresses PNG, JPEG, GIF and SVG images
    .pipe(gulp.dest(`${dstPath}/images/`));
});

gulp.task('copy', function () {
    return gulp.src(`${srcPath}/pdf/**/*`, {
        base: `${srcPath}`
    })
        .pipe(gulp.dest(`${dstPath}`));
});

gulp.task('build', ['css', 'js', 'vendor', 'imgCompression', 'copy']);

gulp.task('default', ['css', 'js', 'vendor', 'imgCompression', 'copy'], function () {
    livereload.listen();
    gulp.watch(`${srcPath}/sass/**/*.scss`, ['css']);
    gulp.watch(`${srcPath}/js/**/*.js`, ['js']);
    gulp.watch('src/**/*.html', ['css']);
    gulp.watch('gulpfile.js', ['css', 'js', 'vendor']);
});
