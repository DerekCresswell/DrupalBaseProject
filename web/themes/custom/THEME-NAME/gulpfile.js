
const gulp = require('gulp');
const sass = require('gulp-sass');
const concat = require('gulp-concat');

// Global variables.
const scssFiles = 'sass/**/*.scss';

/**
 * Compiles SASS into CSS.
 */
gulp.task('sass', function() {

  return gulp.src(scssFiles)
    .pipe(sass())
    .pipe(concat('styles.css'))
    .pipe(gulp.dest('css'));

});

/**
 * Continually compiles SASS to CSS.
 */
gulp.task('sass-watch', function(){

  return gulp.watch(scssFiles, gulp.series('sass'));

});
