/* Copyright 2018 Contributors to Hyperledger Sawtooth

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
----------------------------------------------------------------------------- */


import { call, put } from 'redux-saga/effects';
import RequesterActions from '../redux/RequesterRedux';


/**
 * 
 * Execute base API request
 * 
 * The getBase generator function executes a request to the
 * API to retrieve base data required to hydrate the landing screen.
 * 
 * @param action
 * 
 */
export function * getBase (api, action) {
  try {
    const res = yield call(api.getRequesterBase);

    if (res.ok) {
      console.log('Retrieved base data');
      yield put(RequesterActions.baseSuccess(res.data));
    } else {
      alert(res.data.error);
      yield put(RequesterActions.baseFailure(res.data.error));
    }

  } catch (err) {
    console.error(err);
  }
}


/**
 * 
 * Execute pack API request
 * 
 * The getPack generator function executes a request to the
 * API and handles the response.
 * 
 * @param action
 * 
 */
export function * getPack (api, action) {
  try {
    const { id } = action;
    const res = yield call(api.getPack, id);

    if (res.ok) {
      console.log('Retrieved pack');
      yield put(RequesterActions.packSuccess(res.data));
    } else {
      alert(res.data.error);
      yield put(RequesterActions.packFailure(res.data.error));
    }
  } catch (err) {
    console.error(err);
  }
}
