# Generated by Django 5.0.3 on 2024-03-16 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunSQL(
            """
            CREATE OR REPLACE FUNCTION get_user_registrations_by_month()
            RETURNS TABLE(month varchar, registrations integer) AS
            $$
                BEGIN
                    RETURN QUERY WITH months AS (
                    SELECT generate_series(
                    date_trunc('month', CURRENT_DATE) - INTERVAL '1 year',
                    date_trunc('month', CURRENT_DATE) - INTERVAL '1 month',
                    '1 month'
                    ) AS month_start
                )
                SELECT
                    to_char(months.month_start, 'YYYY-MM')::varchar as month, -- Cast to varchar explicitly
                    COALESCE(count(U.date_joined), 0)::integer as registrations -- Cast to integer explicitly
                FROM
                    months
                LEFT JOIN auth_user U ON
                    date_trunc('month', U.date_joined) = months.month_start
                GROUP BY
                    months.month_start
                ORDER BY
                    months.month_start;
                END;
            $$
            LANGUAGE plpgsql;
            """,
            reverse_sql="DROP FUNCTION IF EXISTS get_user_registrations_by_month();"
        )
    ]
