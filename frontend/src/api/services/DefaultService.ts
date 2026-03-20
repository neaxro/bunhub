/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { DTO_CreateBurger } from '../models/DTO_CreateBurger';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class DefaultService {
    /**
     * Login
     * @returns any Successful Response
     * @throws ApiError
     */
    public static loginShefGet(): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/shef/',
        });
    }
    /**
     * Get All Burgers
     * @param offest
     * @param limit
     * @returns any Successful Response
     * @throws ApiError
     */
    public static getAllBurgersBurgersGet(
        offest?: number,
        limit: number = 10,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/burgers/',
            query: {
                'offest': offest,
                'limit': limit,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Insert Burger
     * @param requestBody
     * @returns any Successful Response
     * @throws ApiError
     */
    public static insertBurgerBurgersPost(
        requestBody: DTO_CreateBurger,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/burgers/',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Burger
     * @param id
     * @returns any Successful Response
     * @throws ApiError
     */
    public static getBurgerBurgersIdGet(
        id: number,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/burgers/{id}',
            path: {
                'id': id,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Burger
     * @param id
     * @returns void
     * @throws ApiError
     */
    public static deleteBurgerBurgersIdDelete(
        id: number,
    ): CancelablePromise<void> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/burgers/{id}',
            path: {
                'id': id,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}
