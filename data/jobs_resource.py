from flask import jsonify
from datetime import datetime
from flask_restful import reqparse, abort, Api, Resource

from data import db_session
from data.jobs import Jobs

parser = reqparse.RequestParser()
parser.add_argument('team_leader', required=True, type=int)
parser.add_argument('job', required=True)
parser.add_argument('work_size', required=True, type=int)
parser.add_argument('collaborators', required=True)
parser.add_argument('start_date', type=datetime)
parser.add_argument('end_date', type=datetime)
parser.add_argument('is_finished', type=bool)


def abort_if_jobs_not_found(job_id):
    session = db_session.create_session()
    jobs = session.query(Jobs).get(job_id)
    if not jobs:
        abort(404, message=f"Jobs {job_id} not found")


class JobsResource(Resource):
    def get(self, job_id):
        abort_if_jobs_not_found(job_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(job_id)
        return jsonify({'jobs': jobs.to_dict(
            rules=('-user.jobs',
                   '-user.hashed_password',
                   '-team_leader.jobs'))})

    def delete(self, job_id):
        abort_if_jobs_not_found(job_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(job_id)
        session.delete(jobs)
        session.commit()
        return jsonify({'success': 'OK'})

    def post(self, job_id):
        args = parser.parse_args()
        if not args:
            return jsonify({'error': 'Empty request'})

        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).get(job_id)

        if not job:
            return jsonify({'error': 'not found'})

        if args.get('team_leader'):
            job.team_leader = args['team_leader']
        if args.get('job'):
            job.job = args['job']
        if args.get('work_size'):
            job.work_size = args['work_size']
        if args.get('collaborators'):
            job.collaborators = args['collaborators']
        if args.get('start_date'):
            job.start_date = args['start_date']
        if args.get('end_date'):
            job.end_date = args['end_date']
        if args.get('is_finished'):
            job.is_finished = args['is_finished']

        db_sess.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'jobs': [item.to_dict(
            rules=('-user.jobs',
                   '-user.hashed_password',
                   '-team_leader.jobs')) for item in jobs]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        job = Jobs(
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
        )

        if args.get('start_date'):
            job['start_date'] = args['start_date']
        if args.get('end_date'):
            job['end_date'] = args['end_date']
        if args.get('is_finished'):
            job['is_finished'] = args['is_finished']
        session.add(job)
        session.commit()
        return jsonify({'id': job.id})
