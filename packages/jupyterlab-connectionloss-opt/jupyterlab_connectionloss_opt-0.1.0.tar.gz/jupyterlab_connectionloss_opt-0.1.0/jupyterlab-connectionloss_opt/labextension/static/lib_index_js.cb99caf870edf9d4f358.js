"use strict";
(self["webpackChunkconnection_opt"] = self["webpackChunkconnection_opt"] || []).push([["lib_index_js"],{

/***/ "./lib/connectionLost.js":
/*!*******************************!*\
  !*** ./lib/connectionLost.js ***!
  \*******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   ConnectionLost: () => (/* binding */ ConnectionLost)
/* harmony export */ });
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__);

/**
 * A default connection lost handler, which brings up an error dialog.
 */
const ConnectionLost = async function (manager, err, translator) {
    translator = translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__.nullTranslator;
    const trans = translator.load('jupyterlab');
    const title = trans.__('Server Connection Error');
    const networkMsg = trans.__('A connection to the Jupyter server could not be established.\n' +
        'JupyterLab will continue trying to reconnect.\n' +
        'Check your network connection or Jupyter server configuration.\n');
    return console.log(title, { message: networkMsg });
};


/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _connectionLost__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./connectionLost */ "./lib/connectionLost.js");


/**
 * Initialization data for the connection-opt extension.
 */
const plugin = {
    id: 'connection-opt:plugin',
    autoStart: true,
    provides: _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.IConnectionLost,
    activate: (app, settingRegistry) => {
        console.log('JupyterLab extension connection-opt is activated!');
        return _connectionLost__WEBPACK_IMPORTED_MODULE_1__.ConnectionLost;
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ })

}]);
//# sourceMappingURL=lib_index_js.cb99caf870edf9d4f358.js.map