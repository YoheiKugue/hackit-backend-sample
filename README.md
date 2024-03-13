ローカルホスト、DB立ち上げ
```bach
docker compose build
docker compose run --entrypoint "poetry init --name hackit-backend-sample  --dependency fastapi --dependency uvicorn[standard]" hackit-backend-sample
docker compose run --entrypoint "poetry install --no-root" hackit-backend-sample
docker compose build –no-cache
docker compose up
```
別のセッションにてマイグレーション
```bach
docker compose exec hackit-backend-sample poetry run python -m api.migrate_db
```