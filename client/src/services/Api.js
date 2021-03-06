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


import apisauce from 'apisauce';


/**
 * 
 * Encapsulated service that eases configuration and other
 * API-related tasks.
 * 
 * @example
 *    const api = API.create(...)
 *    api.login(...)
 *
 * If you would like to use this service in sagas, pass it as an
 * argument and then:
 * 
 * @example
 *    yield call(api.login, ...)
 *  
 */
const create = (baseURL = 'http://localhost:8000/') => {

  /**
   * 
   * Create and configure API object
   * 
   * 
   */
  const api = apisauce.create({
    baseURL
  });


  /**
   * 
   * Definitions
   * 
   * 
   */
  const getRoot = () => api.get('');
  const login = (creds) => api.post('api/authorization', creds);
  const signup = (creds) => api.post('/api/users', creds);
  const getRequesterBase = () => api.get('me/base');
  const getPack = (id) => api.get(`${id}`);
  const search = (query) => api.post('', { q: query });


  return {
    getRoot,
    login,
    getRequesterBase,
    getPack,
    search,
    signup
  }

}

export default {
  create
}
